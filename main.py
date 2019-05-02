import argparse as ap
from gui import *

parser = ap.ArgumentParser()
parser.add_argument("-v", "--vegetarian", help="only display vegetarian foods", action="store_true")
args = parser.parse_args()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
root.destroy()