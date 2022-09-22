from pyflink.datastream import StreamExecutionEnvironment


def pipeline():
    # Create environment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    ds = env.read_text_file('file:///home/user/myfile.json')
    ds.map(lambda i: i).print()

    # Execute job
    env.execute('DynamicStockpilePipeline')


if __name__ == '__main__':
    pipeline()