import argparse

import cryptocompare
import matplotlib.pyplot as plt
import pymannkendall as mk


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--granularity', '-g', type=str, default='minute', help='one of [day,hour,minute], the granularity of the x-axis. default=minute')
    parser.add_argument('--num_points', '-n', type=int, default=60*24, help='number of points to sample from historic prices (e.g. number of days). default=1440')
    parser.add_argument('--mode', '-m', type=str, default='close', help='the cryptocompare price attribute to use (e.g. open or close). default=close')
    parser.add_argument('--currency', '-c', type=str, default='CAD', help='currency (e.g. CAD, USD). default=CAD')

    args = parser.parse_args()

    fig, axs = plt.subplots(2, 1)

    colors = 'rgbykc'
    for ax, symbol, color in zip(axs, ['BTC', 'ETH'], colors):
        fn = getattr(cryptocompare, f'get_historical_price_{args.granularity}')

        btc = fn(symbol, 'CAD', limit=args.num_points)
        data = [x[args.mode] for x in btc]
        cur = data[-1]

        result = mk.original_test(data)
        line = lambda t: result.slope * t + result.intercept
        print(symbol, ':', result, '\n\n')
        ax.plot(data, label=f'{symbol} = {cur} ({result.trend}, p={round(result.p, 4)})', c=color)
        ax.plot(list(map(line, range(len(data)))), label='MK fit')
        ax.legend()
        ax.set_ylabel(f'{symbol} Price ({args.mode})')
        ax.set_xlabel('previous ' + args.granularity + 's')
    fig.suptitle(f'Crypto prices {args.currency} for the last {args.num_points} {args.granularity}s', fontsize=12)
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
