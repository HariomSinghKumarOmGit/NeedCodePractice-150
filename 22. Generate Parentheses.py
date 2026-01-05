class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open ‹ n
        # only add a closing paranthesis if closed ‹ open
        # valid IIF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):

            if openN == closedN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backtrack(openN , closedN+ 1)
                stack.pop()

        backtrack(0, 0)
        return res
    klsjflkkjds 
    slfjsdk 

    sf 
    ksdj setsldkfjjlkdfj
    lskdfj slicelsf
    sf
    fjsl klfjs 
    kfsdlkjkjlksjdfiljs
    sdjfkljsjlsdjfklds
    kdjfiskdsjfksdis slicekf 


    klsjdfidsj
    lljflkdsjodfjslk
    dfjlsksljsdjlkfuwelj
    klsdjfklsjdsdfsdkewjsdfk;slicesdjkfjdsloijflidsfjsijw
    fjdslkjllsjlksdj
    sdlkjf
    lsdkjflkdsjlds
    sortedsdf;fkslk
    slkfjdslkjds
    klsdjfklsdj kjsdfp
    lkjiefkwjiw
    lkdsfjsdlkdsoidsewlkfjfewlk
    lkfjsdlklk
    sdfw
    fssdjilkjewklj
    lkdkljsd

    wsdlkjl
    kldfjlwefjwilksdjfdsl
    jdslkmdsl
    lkcskldj llsdlksfjd
    kldscklsd
    lksdfklsdj
    lkmdslkcsd
    sdlckldsj
    lkcjskljwiwek
    dlkfjweiojiol
    kldsmlkds
    lfwlkjlwe
    ldksmsdklilsd
    sdklcdslkc sortedd ;finallysdflkslkjdsljsdljlfwei
    sdsjdflwep2osf

    sflkdskl 

    sdkfjdskl
    lkfjsdlk
    lkfjskldj
    sdkfjkldsj
    skfjsdkljfsj
    sdfklj l 
    lfjdslkjflksd
    slkjdskljdsllsdjflljdslfkdsjflksdfjlkllsdfjls
    lskd jlksdjf
    sorteds;sdkjjlsdfj lkjkld
    fksd
    ;sdlkjsl
fjdslk 
slj lk kss.kfmds.msms
f.dskm
fmslk
KeyboardInterrupt


sflks KeyboardInterrupt;k;lks

sfkl;sd 
Falses;lfks
lsdkljf
ZeroDivisionError;flkdsj 
sortedfksd;f sorted
sortedfskf ;ZeroDivisionErrorsfk; dslf
ssdlkf;sl sliceslfjksd ;
Falseffs
fksdl;f KeyboardInterrupts


;fklds ;
sdl;fk s;lambdas
ksfs
lksd; 
;sklf s

jjdskljfslkdj
lksdjflksd 
sjdflk sortedflsdkjf sortedlksdjf lkds
kfds lambdasjf lksjfklsj 
sdfj slkd jsk
sklf sortedjflk sj
sk 
fkljds lkj sdklfjs
sdjflksjls
sdlkfjslkdj;
ssdjflskjjsldkfjslkdjjflsjlkefksdjliseufjflksj
dlkfjsdlkfjl
kjsfljslsjdfldsjlsdj