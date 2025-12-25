import re

# Read the source file
with open('gen_hybrid_cultures_l_english.yml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Generate collective nouns
output = ['l_english:\n']
pattern = re.compile(r'(R\d+G\d+B\d+)_hybrid: "(.+?)"')

for line in lines[1:]:  # Skip first line
    match = pattern.search(line)
    if match:
        rgb_id = match.group(1)
        name = match.group(2)
        
        # Apply suffix rules based on name ending and length
        last_char = name[-1].lower()
        last_two = name[-2:].lower() if len(name) >= 2 else name
        
        # Rule-based suffix selection with variety
        if last_two in ['ck', 'pt', 'ct', 'ft', 'xt']:
            suffix = 'ish'
        elif last_char == 'o':
            suffixes = ['vian', 'nian', 'ans']
            suffix = suffixes[hash(name) % 3]
        elif last_char == 'u':
            suffixes = ['vian', 'ans', 'ite']
            suffix = suffixes[hash(name) % 3]
        elif last_char in ['i', 'y']:
            suffixes = ['an', 'tic', 'ans']
            suffix = suffixes[hash(name) % 3]
        elif last_char == 'e':
            suffixes = ['an', 'ese', 'ans']
            suffix = suffixes[hash(name) % 3]
        elif last_char == 'a':
            suffixes = ['n', 'ns', 'ese']
            suffix = suffixes[hash(name) % 3]
        elif len(name) <= 4:
            suffixes = ['ite', 'ese', 'i']
            suffix = suffixes[hash(name) % 3]
        else:
            suffixes = ['ian', 'ans', 'ish', 'ese']
            suffix = suffixes[hash(name) % 4]
        
        collective = f'{name}{suffix}'
        output.append(f'{rgb_id}_hybrid_collective_noun: "{collective}"\n')

# Write to new file
with open('gen_hybrid_cultures_collective_nouns.yml', 'w', encoding='utf-8') as f:
    f.writelines(output)

print(f'Generated {len(output)-1} collective noun entries')
print(f'Output file: gen_hybrid_cultures_collective_nouns.yml')
print('\nFirst 10 examples:')
for i in range(1, min(11, len(output))):
    print(f'  {output[i].strip()}')

