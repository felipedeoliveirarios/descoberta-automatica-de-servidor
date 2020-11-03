git add .
git add -u
echo 'Insira a mensagem do commit:'
read commitMessage
git commit -m "$commitMessage"
git push
echo 'Tudo certo! Pressione ENTER para continuar.'
read