import network
import leaderboard
import amex_loader

print "Loading leader board data"
leader_board_data = leaderboard.load_data_wrapper()
print "Done"

print "Loading training and test data"
training_data, test_data = amex_loader.load_data_wrapper()
print "Done"

net = network.Network([43, 30, 10, 3])

print "Training data"
net.SGD(training_data, 100, 1000, test_data=test_data)

print "Printing Leader board!"
net.leader_print(leader_board_data)
print "Successful!"