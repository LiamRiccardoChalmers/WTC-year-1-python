from user import authentication
from transactions import journal
import banking
#import banking.ubsa.reconciliation
#import banking.online.reconciliation
import sys

amount = 100

if __name__ == "__main__":
    for i,x in enumerate(sys.argv):
        if i != 0:
            print(sys.argv[i])
    authentication.authenticate_user()
    journal.receive_income(amount)
    journal.pay_expense(amount)
    #banking.reconciliation.do_reconciliation()
    banking.fvb.reconciliation.do_reconciliation()
    #banking.ubsa.reconciliation.do_reconciliation()
    #banking.online.reconciliation.do_reconciliation()
    #help("modules")
