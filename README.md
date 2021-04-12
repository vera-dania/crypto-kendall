# crypto-kendall
Runs Mann-Kendall trend detection and shows plots of BTC/ETH using cryptocompare, pymannkendall, and matplotlib

```
usage: crypto_kendall [-h] [--granularity GRANULARITY]
                      [--num_points NUM_POINTS] [--mode MODE]
                      [--currency CURRENCY]

optional arguments:
  -h, --help            show this help message and exit
  --granularity GRANULARITY, -g GRANULARITY
                        one of [day,hour,minute], the granularity of the
                        x-axis. default=minute
  --num_points NUM_POINTS, -n NUM_POINTS
                        number of points to sample from historic prices (e.g.
                        number of days). default=1440
  --mode MODE, -m MODE  the cryptocompare price attribute to use (e.g. open or
                        close). default=close
  --currency CURRENCY, -c CURRENCY
                        currency (e.g. CAD, USD). default=CAD
```
