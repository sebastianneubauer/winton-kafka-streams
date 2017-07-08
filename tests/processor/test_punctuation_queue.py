
import winton_kafka_streams.processor._punctuation_queue as punctuation_queue

def test_punctuation_queue():
    punctuations = []
    pq = punctuation_queue.PunctuationQueue(lambda ts, node: punctuations.append((ts, node)))
    pq.schedule('node', 100)
    now = -100

    pq.may_punctuate(now)
    assert len(punctuations) == 0

    pq.may_punctuate(now + 99)
    assert len(punctuations) == 0

    pq.may_punctuate(now + 100)
    assert len(punctuations) == 1

    pq.may_punctuate(now + 199)
    assert len(punctuations) == 1

    pq.may_punctuate(now + 200)
    assert len(punctuations) == 2

    assert punctuations == [('node', 0), ('node', 100)]
