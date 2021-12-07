f = open("input07.txt", "r")
    l = readlines(f)
close(f)

positions = [parse(Int, n) for n in split(l[1], ",")]

options = collect(minimum(positions):maximum(positions))
consumption = zeros(length(options))
for (i, k) in enumerate(options)
    diff = positions - ones(length(positions)) * k
    fuel = sum([abs(j) for j in diff])
    consumption[i] = fuel
end

best_fuel = minimum(consumption)
println("Result 1: $best_fuel")


consumption = zeros(length(options))
for (i, k) in enumerate(options)
    diff = positions - ones(length(positions)) * k
    eachfuel = [sum(collect(1:abs(j))) for j in diff]
    fuel = sum([abs(j) for j in eachfuel])
    consumption[i] = fuel
end

new_best_fuel = minimum(consumption)
println("Result 2: $new_best_fuel")
