class Solution:
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    l = 1
    r = n
    while(l<r):
      mid = (l+r)//2
      if(not isBadVersion(mid)):
        l = mid + 1
      else:
        r = mid
    return l