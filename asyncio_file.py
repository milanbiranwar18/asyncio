import asyncio

async  def main():
    """
    Function for implementing async and await
    """
    print("Hello")
    await asyncio.sleep(5)
    print("World")


if __name__ == '__main__':
    asyncio.run(main())