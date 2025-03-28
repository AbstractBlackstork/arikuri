defmodule GameFileScanner do
  @game_path "C:/Program Files (x86)/Steam/steamapps/common/Crusader Kings III/game"
  @context_lines 5  # Number of lines to show before and after matches

  def scan_file(relative_path) do
    path = Path.join(@game_path, relative_path)
    case File.read(path) do
      {:ok, content} ->
        IO.puts("=== Content of #{relative_path} ===\n")
        IO.puts(content)
        IO.puts("\n=== End of file ===")
      {:error, reason} ->
        IO.puts("Error reading #{path}: #{reason}")
    end
  end

  def search_pattern(relative_path, pattern, show_context \\ true) do
    path = Path.join(@game_path, relative_path)
    case File.read(path) do
      {:ok, content} ->
        lines = content |> String.split("\n")
        matches = lines
        |> Enum.with_index(1)
        |> Enum.filter(fn {line, _} ->
          String.contains?(String.downcase(line), String.downcase(pattern))
        end)

        if Enum.empty?(matches) do
          IO.puts("No matches found for '#{pattern}' in #{relative_path}")
        else
          IO.puts("=== Matches for '#{pattern}' in #{relative_path} ===\n")
          Enum.each(matches, fn {line, line_num} ->
            if show_context do
              show_context(lines, line_num, line)
            else
              IO.puts("Line #{line_num}: #{line}")
            end
          end)
          IO.puts("\n=== End of matches ===")
        end
      {:error, reason} ->
        IO.puts("Error reading #{path}: #{reason}")
    end
  end

  def search_directory(dir_path, pattern) do
    full_path = Path.join(@game_path, dir_path)
    case File.ls(full_path) do
      {:ok, files} ->
        files
        |> Enum.filter(&String.ends_with?(&1, ".txt"))
        |> Enum.each(fn file ->
          file_path = Path.join(dir_path, file)
          search_pattern(file_path, pattern)
        end)
      {:error, reason} ->
        IO.puts("Error reading directory #{full_path}: #{reason}")
    end
  end

  def recursive_search(dir_path, pattern) do
    full_path = Path.join(@game_path, dir_path)
    case File.ls(full_path) do
      {:ok, files} ->
        files
        |> Enum.each(fn file ->
          file_path = Path.join(dir_path, file)
          full_file_path = Path.join(@game_path, file_path)
          cond do
            String.ends_with?(file, ".txt") ->
              search_pattern(file_path, pattern)
            File.dir?(full_file_path) ->
              recursive_search(file_path, pattern)
            true -> :ok
          end
        end)
      {:error, reason} ->
        IO.puts("Error reading directory #{full_path}: #{reason}")
    end
  end

  defp show_context(lines, line_num, current_line) do
    start_idx = max(0, line_num - @context_lines - 1)
    end_idx = min(length(lines) - 1, line_num + @context_lines - 1)

    IO.puts("\nMatch at line #{line_num}:")
    IO.puts("#{String.duplicate("-", 50)}")

    Enum.slice(lines, start_idx..end_idx)
    |> Enum.with_index(start_idx + 1)
    |> Enum.each(fn {line, idx} ->
      prefix = if idx == line_num, do: "=>", else: "  "
      IO.puts("#{prefix} #{String.pad_leading("#{idx}", 4)}: #{line}")
    end)

    IO.puts("#{String.duplicate("-", 50)}")
  end
end

# Main execution
IO.puts("\n=== Checking Tenet-Doctrine Hostility Interactions ===")

IO.puts("\n1. Checking tenet_gnosticism hostility overrides...")
GameFileScanner.search_directory("common/religion/doctrines", "tenet_gnosticism")

IO.puts("\n2. Checking special_doctrine_is_gnostic_faith hostility overrides...")
GameFileScanner.search_directory("common/religion/doctrines", "special_doctrine_is_gnostic_faith")

IO.puts("\n3. Checking all hostility_override_tenet patterns...")
GameFileScanner.search_directory("common/religion/doctrines", "hostility_override_tenet")

IO.puts("\n4. Checking all hostility_override_special_doctrine patterns...")
GameFileScanner.search_directory("common/religion/doctrines", "hostility_override_special_doctrine")

# Example usage:
# Read a specific file:
# GameFileScanner.scan_file("common/religion/doctrines/02_doctrines_special.txt")

# Search for a pattern in a specific file:
# GameFileScanner.search_pattern("common/religion/doctrines/01_doctrines_religions.txt", "gnostic")

# Search for a pattern in all .txt files in a directory:
# GameFileScanner.search_directory("common/religion/doctrines", "gnostic")

# Search recursively through all subdirectories:
# GameFileScanner.recursive_search("common/religion", "gnostic")
