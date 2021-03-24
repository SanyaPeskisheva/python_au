import sys

LEETCODE_END_LINK = '[comment]: <> (Stop)'


class LeetCodeSolution:
    def __init__(self, title, link, code):
        self.title = title.split('. ')[1].rstrip('\n')
        self.link = link.rstrip('\n')
        self.code = '``` python\n{}\n```'.format('\n'.join(map(lambda x: x.strip('\n')[4:], code)))

    def __str__(self):
        return 'title = {}, link = {}, code = {},'.format(self.title, self.link, self.code)

    def get_md_title(self):
        return '## {}\n'.format(self.title)

    def get_md_solution_link(self):
        return '+ [{}](#{})'.format(self.title, self.link[30:-1])

    def get_md_formatted_solution(self):
        return ('{}\n{}\n\n{}\n\n{}\n'.format(self.get_md_title(), self.get_md_solution_link(), self.link,
                                            self.code))


def read_all_lines_from(filename):
    file = open(filename)
    result = file.readlines()
    file.close()
    return result


def write_to_md(filename, data):
    file = open(filename, "w")
    main_title = ''
    upper_next = True
    for letter in filename:
        if upper_next:
            main_title += letter.upper()
            upper_next = False
            continue
        if letter == '.':
            break
        if letter == '-':
            main_title += ' '
            upper_next = True
            continue
        main_title += letter
    file.write("# {}\n".format(main_title))
    file.write(data)
    file.close


def read_all_file(filename):
    file = open(filename)
    result = file.read()
    file.close()
    return result


def merge_solutions(old_solution, new_solution):
    new_solution = new_solution.split('\n')
    old_solution = old_solution.split('\n')
    new = ''
    i = 2
    while True:
        if old_solution != ['']:
            if old_solution[i] != '':
                if old_solution[i][0] == '+' :
                    new += '\n' + old_solution[i]
                    i += 1
            else: break
        else: break
    new += '\n' + new_solution[2]+ '\n'
    for k in range(i, len(old_solution)):
        new +=  '\n' + old_solution[k]
    new += '\n' + new_solution[0] + '\n'
    for i in range(3, len(new_solution)):
        new += new_solution[i] + '\n'
    return(new)


def main(input_filename, output_filename):
    in_txt = read_all_lines_from(input_filename)
    source = LeetCodeSolution(in_txt[0], in_txt[1], in_txt[3:])
    new = source.get_md_formatted_solution()
    old = read_all_file(output_filename)
    result = merge_solutions(old, source.get_md_formatted_solution())
    write_to_md(output_filename, result)


if __name__ == "__main__":
    params = sys.argv
    params = ['','src.txt','intervals.md']
    main(params[1],params[2])
