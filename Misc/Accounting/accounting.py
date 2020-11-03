from user import authentication
from transactions import journal
import banking
#import banking.fvb.reconciliation
#import banking.ubsa.reconciliation
#import banking.online.reconciliation
import sys
import user_management.management
import invoice.account
import trial_balance.balance
import multiple_currency_support.exchange_rate
import asset_management.assets
import reporting.complaint

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
    user_management.management.user_managament()
    invoice.account.account(amount)
    trial_balance.balance.do_balance(amount)
    multiple_currency_support.exchange_rate.dollar()
    asset_management.assets.asset_check()
    reporting.complaint.do_report()

#this is a comment

#how about another one?

#three is asking for to much

