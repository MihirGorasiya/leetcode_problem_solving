def boyerMooreVoting(nums):
    count = 0
    candidate = None

    for i in nums:
        if count == 0:
            candidate = i

        if i == candidate:
            count += 1
        else:
            count -= 1

    return candidate


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]

    print(boyerMooreVoting(nums))
