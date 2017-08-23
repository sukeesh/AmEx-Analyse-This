import network
import leaderboard
import amex_loader

print "Loading leader board data"
leader_board_data = leaderboard.load_data_wrapper()
print "Done"

print "Loading training and test data"
training_data, test_data = amex_loader.load_data_wrapper()
print "Done"

net = network.Network([25, 20, 15, 10, 5, 3])
net.SGD(training_data, 100, 20, test_data=test_data)

print "Training data"

print "Printing Leader board!"
net.leader_print(leader_board_data)
print "Successful!"