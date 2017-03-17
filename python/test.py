import tensorflow as tf
hello = tf.constant("Hello, jasmine")
sess = tf.Session()
print "==============================="
print sess.run(hello)
print ""
print "= SUCCESS SETUP ="
print "==============================="

# import tensorflow as tf

# # Variable = 0
# state = tf.Variable(0, name="counter")

# # op add 1 to state
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)

# # op init all Variable
# init_op = tf.initialize_all_variables()

# # start session
# with tf.Session() as sess:
#   # init
#   sess.run(init_op)
#   # print init state
#   print sess.run(state)
#   # run update and print state
#   for _ in range(3):
#     sess.run(update)
#     print sess.run(state)
