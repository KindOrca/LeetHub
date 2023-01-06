class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M',
            4:'IV',
            9:'IX',
            40:'XL',
            90:'XC',
            400:'CD',
            900:'CM',
            0:''
        }
        ans = ''
        start = 1000
        while start:
            temp = (num // start) * start
            if temp in dic:
                ans = ans + dic[temp]
            else:
                if temp > 5*start:
                    ans = ans + dic[5*start] + dic[start]*((temp//start)%5)
                else:
                    ans = ans + dic[start]*((temp//start))
            num %= start
            start //= 10
        return ans