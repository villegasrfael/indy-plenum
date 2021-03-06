def emulate_catchup(replica, ppSeqNo=100):
    replica.on_catch_up_finished(last_caught_up_3PC=(replica.viewNo, ppSeqNo),
                                 master_last_ordered_3PC=replica.last_ordered_3pc)


def emulate_select_primaries(replica):
    replica.primaryName = 'SomeAnotherNode'
    replica._setup_for_non_master_after_view_change(replica.viewNo)


def expect_suspicious(replica, suspicious_code):
    def reportSuspiciousNodeEx(ex):
        assert suspicious_code == ex.code
        raise ex

    replica.node.reportSuspiciousNodeEx = reportSuspiciousNodeEx
