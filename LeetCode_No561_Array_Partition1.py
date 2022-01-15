# 문제 : 숫자 2개씩 짝지어 min(a,b)를 한 뒤 다 더했을 때 가장 큰 값을 구하기
# 가장 큰 값이려면, min(a,b)에서 a와 b의 차이가 가장 적으면 된다.
# 차이가 가장 적으려면, 정렬을 한 뒤 바로 옆에 있는 수가 될 것이다.
# 그러므로 정렬을 한 뒤 홀수번째 위치한 숫자(인덱스 상으로는 짝수)를 다 더하면 된다.

class Solution:
    def arrayPairSum(self, nums) -> int:
        return sum(sorted(nums)[::2]) # 처음부터 리스트 끝까지 홀수번째 숫자(인덱스는 짝수)인 수를 다 더한다.

a = Solution()
print(a.arrayPairSum([1,4,6,3,2,5]))