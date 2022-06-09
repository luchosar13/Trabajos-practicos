job('ejemplo-job-DSL') {
  description('Job DSL ejemplo para el curso de jenkins')
  scm {
    git('https://github.com/macloujulian/jenkins.job.parametrizado.git', 'main') { node ->
      node / gitConfigName('macloujulian')
      node / gitConfigEmail('macloujulian@gmail.com')
	  }
  }
  parameters {
    stringParam('nombre', defaultValue = 'Luciano', description('Parametro de cadena para el Job'))
    choiceParam('planeta', ['Tierra','Marte','Jupiter','Venus','Saturno'])
    booleanParam('agente', false)
    }
  triggers {
    cron('H/7 * * * *')
  }
  steps {
    shell("bash jobscript.sh")
  }
  publishers {
    mailer('aprendizajeml3@gmail.com', true, true)
  }
}
