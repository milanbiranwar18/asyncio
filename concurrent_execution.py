import logging
import time
import asyncio

logging.basicConfig(filename="django.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


async  def display_time():
    """
    Function for how many seconds are passed and to await for 1 second
    """
    try:
        stat_time = time.time()

        while True:
            dur = int(time.time() - stat_time)

            if dur % 3 == 0:
                print("{} seconds have passed".format(dur))

            await  asyncio.sleep(1)

    except Exception as e:
        logging.error(e)


async def print_num():
    """
    Function for awaiting numbers for 0.1 second
    """
    try:
        num = 1

        while num<=100:
            print(num)
            num += 1
            await  asyncio.sleep(0.1)

    except Exception as e:
        logging.error(e)


async  def main():
    """
    Function for taking multiple awaitable objects and to run them concurrently
    """
    try:
        task1 = asyncio.create_task(display_time())
        task2 = asyncio.create_task(print_num())

        await  asyncio.gather(task1, task2)

    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    asyncio.run(main())