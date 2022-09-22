from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode
from pyflink.datastream.connectors import FileSource, StreamFormat, FileSink
from pyflink.common import WatermarkStrategy, Encoder, Types

def load_csv_in_flink(path):
    # Create environment
    env = StreamExecutionEnvironment.get_execution_environment()
    #env.set_runtime.mode(RuntimeExecutionMode.BATCH)
    env.set_parallelism(1)


    ds = env.from_source(source = FileSource.for_record_stream_format(StreamFormat.text_line_format(), path)
                    .process_static_file_set()
                    .build(),
                    watermark_strategy=WatermarkStrategy.for_monotonous_timestamps(),
                    source_name='csv_file')

       
    ds.print()

    # Execute job
    env.execute()

if __name__ == '__main__':
    load_csv_in_flink("./myfile.csv")