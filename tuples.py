# list r tuples almost same but list er data mutable but tuples er data immutable
# list er jnne []. dictionary er jnne {} r tuples er jnne ()
# tuples list er theke much faster kaj kore
#  tuple er majhe r o tuple rakha jay

students = (
    ("Mahbub Hossain", 1029, "JU"), "Randhunibari", "Sirajganj"
)

# students[3] = "ki jani ki hy janina" TypeError: 'tuple' object does not support item assignment
print(students[1])
