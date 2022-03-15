from tests.flow.flo import Flo


def test_one_and_done():
    Flo.test("tests/flow/bank_first_for_two_rounds.sim.txt")
