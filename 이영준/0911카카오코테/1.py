def solution(id_list, report, k):
    reported = {user: set() for user in id_list}
    for r in report:
        # 신고한 유저, 신고 당한 유저
        report_user, bad_user = r.split()
        reported[bad_user].add(report_user)
    # k번 이상 신고 당한 경우 메일 발송
    mail_send = {user: 0 for user in id_list}
    for user in reported:
        if len(list(reported[user])) >= k:
            for u in reported[user]:
                mail_send[u] += 1
    
    answer = []
    for id in id_list:
        answer.append(mail_send[id])
    return answer
