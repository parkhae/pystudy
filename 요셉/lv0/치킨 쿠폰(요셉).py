def solution(chicken):
    answer = 0
    coupon = chicken
    while coupon > 10:
        chicken_, coupon_ = divmod(coupon, 10)
        answer += chicken_
        coupon = chicken_ + coupon_
        print(chicken, coupon_)
    answer += coupon//10
    return answer