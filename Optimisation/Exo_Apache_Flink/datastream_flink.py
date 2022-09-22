from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from statistics import mean

if __name__ == "__main__":
    
    # generate the input file.
    src_data = [
                [1, 4, 2, 1], #time series 1
                [3, 5, 1, 3], #time series 2, etc
                [6, 1, 2, 4]
               ]

    # set up the environment 
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
   
   # read data from source
    ds = env.from_collection(
        collection=src_data,
        type_info=Types.ROW([Types.INT(), Types.INT(), Types.INT(), Types.INT()])
        )

    # get the mean, the min and the max
    ds2 =  ds \
            .map(lambda i: (i[0] + i[1] + i[2] + i[3])/len(i))\
            .map(lambda i: min(i))\
            .map(lambda i: max(i))\
            .print()


    env.execute()