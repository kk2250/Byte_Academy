import model
import view


# Note: we could write the following as well:
# while True:
def game_loop():
    while 1:
        import time
        time.sleep(1)
        print('This... \n is.., \n an... \n ')



        buy_inputs = ['b', 'buy']
        sell_inputs = ['s', 'sell']
        lookup_inputs = ['l', 'lookup','look up', 'look-up']
        quote_inputs = ['q', 'quote']
        exit_inputs = ['e','exit','quit']
        acceptable_input = buy_inputs      \
                            +sell_inputs   \
                            +lookup_inputs \
                            +quote_inputs  \
                            +exit_inputs
        user_input = view.main_menu()
        if user_input in acceptable_inputs:
            if user_input in buy_inputs:
                (ticker_symbol, trade_volume) = view.transaction_menu()
                print(ticker_symbol, trade_volume)
                confirmaion_message = model.buy(ticker_symbol,trade_volume)
                pass

            elif user_input in sell_inputs:
                pass

            elif user_input in lookup_inputs:
                return model.lookup(view.lookup_menu())

            elif user_input in quote_inputs:
                return model.quote(view.quote_menu())

            elif user_input in exit_inputs:
                break


        option_1 = view.main_menu()


        if option_1 == 'l':
            company_name = view.lookup_menu()
            return model.lookup(company_name)

        elif option_1 == 'q':
            ticker_symbol = view.quote_menu()
            return model.quote(ticker_symbol)