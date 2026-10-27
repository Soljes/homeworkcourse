class PersonInfo:
    def __init__(self, fi, age, *deps):
        self.fi = fi
        self.age = age
        self.deps = deps

    def short_name(self):
        parts = self.fi.split()

        first_letter = parts[0][0]
        last_name = parts[1]

        name = f"{last_name} {first_letter}."
        return name

    def path_deps(self):
        """Путь до подразделения"""
        return " --> ".join(self.deps)

    def new_salary(self):
        """Новая зарплата"""
        all_deps_text = "".join(self.deps)

        char_counts = {}
        for char in all_deps_text:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

        counts_list = list(char_counts.values())
        counts_list.sort(reverse=True)

        top_three_counts = counts_list[:3]
        total_top_letters = sum(top_three_counts)

        return 1337 * self.age * total_top_letters