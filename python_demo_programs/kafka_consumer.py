#!/usr/bin/env python
from kafka import KafkaConsumer


def main():
    consumer = KafkaConsumer(bootstrap_servers='10.5.70.113:9092',
                             auto_offset_reset='latest')
    consumer.subscribe(['auditlog_RB'])

    n = 2
    for message in consumer:
        # print(message.value)
        fields = message.value.decode("ISO-8859-1").split('\t')
        stages = fields[20]
        stages = stages.split(',')
        for stage in stages:
            if not stage == '':
                if int(stage[2:], 16) == 68:
                    candidate_adunits = [int(fields[49][i:i + n], 16) for i in range(0, len(fields[49]), n)]
                    print("dsp: " + str(int(stage[:2], 16)) + " stage: " + str(int(stage[2:], 16)) +
                          " candidate ad units: " + str(candidate_adunits) )

    consumer.close()


if __name__ == "__main__":
    main()