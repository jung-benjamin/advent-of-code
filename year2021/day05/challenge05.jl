f = open("input05.txt", "r")
    l = readlines(f)
close(f)

coordinates = Array{Int}(undef, length(l), 4)

for (i, line) in enumerate(l)
    (s1, s2) = split(line, "->")
    x1 = parse(Int, split(s1, ",")[1])
    y1 = parse(Int, split(s1, ",")[2])
    x2 = parse(Int, split(s2, ",")[1])
    y2 = parse(Int, split(s2, ",")[2])
    coordinates[i,:] = [x1, y1, x2, y2]
end

max_coord = maximum(coordinates)

vent_map = zeros((max_coord+1, max_coord+1))

coordinates += ones(size(coordinates))
coordinates = trunc.(Int, coordinates)
for row in eachrow(coordinates)
    if row[1] == row[3]
        if row[2] > row[4]
            plus = ones(size(vent_map[row[4]:row[2],row[1]:row[3]]))
            vent_map[row[4]:row[2],row[1]:row[3]] += plus
        elseif row[4] > row[2]
            plus = ones(size(vent_map[row[2]:row[4],row[1]:row[3]]))
            vent_map[row[2]:row[4],row[1]:row[3]] += plus
        end
    elseif row[2] == row[4]
        if row[3] > row[1]
            plus = ones(size(vent_map[row[2]:row[4],row[1]:row[3]]))
            vent_map[row[2]:row[4],row[1]:row[3]] += plus
        elseif row[1] > row[3]
            plus = ones(size(vent_map[row[2]:row[4],row[3]:row[1]]))
            vent_map[row[2]:row[4],row[3]:row[1]] += plus
        end
    end
end
counter = 0
for i in vent_map
    if i >= 2
        global counter += 1
    end
end
println("Result 1: $counter")

for row in eachrow(coordinates)
    if row[1] != row[3] && row[2] != row[4]
        if row[1] > row[3]
            x = collect(row[1]:-1:row[3])
        else
            x = collect(row[1]:row[3])
        end
        if row[2] > row[4]
            y = collect(row[2]:-1:row[4])
        else
            y = collect(row[2]:row[4])
        end
        for (i, j) in zip(y, x)
            vent_map[i, j] += 1
        end
    end
end
counter = 0
for i in vent_map
    if i >= 2
        global counter += 1
    end
end
println("Result 2: $counter")
