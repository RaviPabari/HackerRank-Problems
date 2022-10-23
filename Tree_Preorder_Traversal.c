void preOrder( struct node *root) {
    if(root == NULL){
        return;
    }
    else{
    printf("%d ",root->data);
    preOrder(root->left);
    preOrder(root->right);
    }
}
