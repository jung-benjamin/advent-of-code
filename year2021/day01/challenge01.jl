
f = open("input01.txt", "r")
    l = readlines(f)
close(f)

# Part 1
a = collect(zip(l, l[2:end]))
larger = 0
smaller = 0
for l in a
    i = parse(Int, l[1])
    j = parse(Int, l[2])
    if i < j
        global larger += 1
    elseif i > j
        global smaller += 1
end
end
println("Larger : $larger")
println("Smaller : $smaller")

# Part 2
s = 0
larger_2 = 0
smaller_2 = 0
b = collect(zip(l, l[2:end], l[3:end]))
for l in b
    ii = parse(Int, l[1])
    jj = parse(Int, l[2])
    kk = parse(Int, l[3])
    ss = ii + jj + kk
    if s == 0
        global s = ss
    elseif s < ss
        global larger_2 += 1
        global s = ss
    elseif s > ss
        global smaller_2 += 1
        global s = ss
    end
end
println("Larger_2 : $larger_2")
println("Smaller_2 : $smaller_2")
