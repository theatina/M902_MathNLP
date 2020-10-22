import argparse

#Exercises
class Exercises:
    def ex_1_1(sentence="Μια παπια μα ποια παπια; Μια παπια με παπια."):
        A = set(sentence)
        cardinal_number_A = len(A)
        print("\nA = " + str(A))
        print("\nΠληθικός αριθμός συνόλου A: " + str(cardinal_number_A) + "\n")
        return 1

    def ex_1_2(sentence="Δεν προλαβαίνω ποτέ δεν προλαβαίνω"):
        words = sentence.split(" ")
        A = set(words)
        cardinal_number_A = len(A)
        print("\n A = " + str(A))
        print("\nΠληθικός αριθμός συνόλου A: " + str(cardinal_number_A) + "\n")
    
        return 2

    #making use of capital letters, in order not to have to deal with the two s 's, "σ" and "ς"
    def ex_1_3(sentence="οι πολιτικες και οικονομικες εξελιξεις διαδραματιζονται γυρω απο τις προσπαθειες, τις βλεψεις και τους αγωνες για τον ελεγχο των φυσικων πορων"):
        alphabet = set("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")
        A = set(sentence.upper())
        common_letters = alphabet.intersection(A)
        non_common_letters = alphabet-common_letters
        print(non_common_letters)
        cardinal_number_common_letters = len(common_letters)
        print("\n A = " + str(A))
        print("\nΠληθικός αριθμός συνόλου γραμμάτων που περιέχονται στη φράση: " + str(cardinal_number_common_letters))
        if cardinal_number_common_letters is len(alphabet):
            print("\nThe sentence: '" + sentence + "' is a Pangram ! \n")
            return True
        else:
            print("\nThe sentence: '" + sentence + "' is ΝΟΤ a Pangram ! \n\n( set of missing letters: " + str(non_common_letters) + " )\n")
            return False

    def ex_1_4():
        print("\nΔε μπορούμε να συμπεράνουμε ότι μια φράση είναι pangram εάν έχει απλά πληθικό αριθμό συνόλου χαρακτήρων 24, καθώς μπορεί να περιέχει και άλλους χαρακτήρες όπως σημεία στίξης (';', '.', ',', κλπ)\n")

    def ex_1_5():
        A = [ 'ενα', 'νεα', 'εννεα']
        print("\n3 λέξεις με σύνολο γραμμάτων το {α, ε, ν}: " + str(A) + "\n")

    def ex_1_6():
        A = [ 'ΠΡΑΣΟ', 'ΣΠΑΡΟΣ', 'ΠΡΑΟΣ', 'ΑΣΠΡΟΣ']
        print("\nΛέξεις με σύνολο γραμμάτων το {Α, Ο, Π, Ρ, Σ}: " + str(A) + "\n")

    def ex_1_7():
        A = [ 'ΠΛΟΙΟ', 'ΠΑΛΙΟΙ', 'ΠΑΛΙΟ', 'ΛΟΙΠΟΙ', 'ΠΟΛΛΟΙ']
        print("\nΛέξεις με σύνολο γραμμάτων το {Π, Ι, Λ, Ο}, με μήκος > 4: " + str(A) + "\n")


    def ex_1_8():
        words = ['νερο', 'ποταμι', 'οργη']
        vowels_gr = set('αεηιουω')
        A = set()
        for word in words:
            A.update(word)
            
        vowels_not_in_words = vowels_gr - A.intersection(vowels_gr)
        print(vowels_not_in_words)


#main
parser = argparse.ArgumentParser()
parser.add_argument("-ex", type=int, help="number of exercise to solve", default=1)
args = parser.parse_args()

if (args.ex > 10) or (args.ex < 1):
    print("\nExercises between 1 - 10 ! !\n")
    exit()

function_to_call_name = "ex_1_" + str(args.ex)
fun_to_call = getattr(Exercises, function_to_call_name)
fun_to_call()