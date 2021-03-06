def _impl(ctx):
  #request_skeleton = ctx.outputs.output
  for f in ctx.attr.srcs:
    sourceFilename = ctx.expand_location(ctx.attr.command, [f])
    tree = ctx.actions.declare_directory(ctx.attr.name)
    ctx.actions.run(
      inputs = ctx.files.srcs,
      #outputs = [ request_skeleton ],
      outputs = [ tree ],
      arguments = [ 
		 "--gen",
		 "py:new_style",
		 "-out",
                 #"external/contrail_repository/src/config",
                 ".",
		 sourceFilename,
		 ],
      progress_message = "Generating sandesh files into '%s'" % sourceFilename,
      executable = ctx.executable._tool,
    )

  return [ DefaultInfo(files = depset([ tree, ])) ]

gensandesh = rule(
  implementation = _impl,
  attrs = {
    "_tool": attr.label(
      executable = True,
      cfg = "host",
      allow_files = True,
      #default = Label("//contrail/configapi:sandeshbin"),
      default = Label("//contrail/sandesh:sandeshbin"),
    ),
    "srcs": attr.label_list(allow_files = True),
    "command": attr.string(),
    "output": attr.output(doc = "The generated file"),
  },
  #outputs = {"request_skeleton": "acl/request_skeleton.py"},
)
