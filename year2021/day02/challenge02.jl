f = open("input02.txt", "r")
    l = readlines(f)
close(f)

horizontal = 0
deep = 0
for a in l
    s = split(a, " ")
    if s[1] == "forward"
        global horizontal += parse(Int, s[2])
    elseif s[1] == "down"
        global deep += parse(Int, s[2])
    elseif s[1] == "up"
        global deep += -parse(Int, s[2])
    else
        println("Unknown entry in input")
    end
end
product = horizontal * deep
println("Part 1")
println("Horizontal : $horizontal")
println("Depth : $deep")
println("Product : $product")

horizontal = 0
deep = 0
aim = 0
for a in l
    s = split(a, " ")
    if s[1] == "down"
        global aim += parse(Int, s[2])
    elseif s[1] == "up"
        global aim += -parse(Int, s[2])
    elseif s[1] == "forward"
        global horizontal += parse(Int, s[2])
        global deep += (parse(Int, s[2]) * aim)
    else
        println("Unknown entry in input")
    end
end
product = horizontal * deep
println("Part 2")
println("Horizontal : $horizontal")
println("Depth : $deep")
println("Product : $product")

