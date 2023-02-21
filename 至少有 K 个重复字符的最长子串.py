# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
#
#  
#
# 示例 1：
#
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 示例 2：
#
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 方法二：滑动窗口
# 我们枚举最长子串中的字符种类数目，它最小为 11，最大为 |\Sigma|∣Σ∣（字符集的大小，本题中为 2626）。
#
# 对于给定的字符种类数量 tt，我们维护滑动窗口的左右边界 l,rl,r、滑动窗口内部每个字符出现的次数 \textit{cnt}cnt，以及滑动窗口内的字符种类数目 \textit{total}total。当 \textit{total} > ttotal>t 时，我们不断地右移左边界 ll，并对应地更新 \textit{cnt}cnt 以及 \textit{total}total，直到 \textit{total} \le ttotal≤t 为止。这样，对于任何一个右边界 rr，我们都能找到最小的 ll（记为 l_{min}l
# var longestSubstring = function(s, k) {
#     if(k<=1){ return s.length; }
#     else if(s.length < k){ return 0; }
#     const map = {};
#     // 计算每种字符出现次数
#     for(let i=0; i<s.length; i+=1){
#         map[s[i]] ? map[s[i]]+=1 : map[s[i]] = 1;
#     }
#     // 收集不满足的字符
#     const keys = [];
#     for(key in map){
#         if(map[key] < k){
#             keys.push(key);
#         }
#     }
#     return keys[0]
#     ? Math.max(// 分割求最大
#         ...s.split(new RegExp(keys.join('|'), 'g'))
#             .map(x => longestSubstring(x, k))
#         )
#     : s.length;
# };
#


