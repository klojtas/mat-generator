import  getopt,sys
import random

class generate_math:
    exercises_per_group = 20
    min = 5
    max = 10
    output = 'console'
    debug = False
    @staticmethod
    def usage():
        print(
            "generate_math.py -o <output> -d <dest_sys> -c <channel_list> -f <file> -u <username> -p <password> "
            "--changelist <value> --mode <create|update> --desc-opt <blank|ESBReady|skip> --custom-desc <text>"
            "--status-opt <active|inactive|ignore> --change-list-dest <channel_list> --debug")
    def __init__(self, argv):

        try:
            opts, args = getopt.getopt(argv, "o",
                                       ["max=", "min=","output="])
        except getopt.GetoptError as err:
            print(err)
            generate_math.usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                generate_math.usage()
                sys.exit()
            elif opt in ("-o", "--output="):
                self.output = arg.lower()
            elif opt in ("--max"):
                self.max = arg.lower()
            elif opt in ("--min"):
                self.min = arg
        self.parameters_check()
    def parameters_check(self):
        if self.output is None or self.max is None or self.min is None:
            generate_math.usage()
            sys.exit(2)
    def generate(self):
       # random sum
       for x in range(self.exercises_per_group):
           random_sum = random.randint(self.min,self.max)
           random_left = random.randint(1,random_sum)
           random_right = random_sum - random_left
           line="{} + {} = __".format(random_left,random_right)

       # random right
           random_sum = random.randint(self.min,self.max)
           random_left = random.randint(1,random_sum)
           line=line+"\t\t{} + __ = {}".format(random_left,random_sum)

       # random left
           random_sum = random.randint(self.min,self.max)
           random_right = random.randint(1,random_sum)
           line=line+"\t\t__ + {} = {}".format(random_right,random_sum)

       # random double right

           random_sum = random.randint(self.min, self.max)
           random_left = random.randint(1, random_sum)
           random_sum_left = random.randint(1, random_sum)
           random_sum_right = random_sum - random_sum_left
           line=line+"\t\t{} + __ = {} + {}".format(random_left, random_sum_left, random_sum_right)
           print(line)


if __name__ == '__main__':
    math = generate_math(sys.argv[1:])
    math.generate()
    print("Finished!")
