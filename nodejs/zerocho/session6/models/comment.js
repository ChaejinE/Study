const Sequelize = require("sequelize");

class Comment extends Sequelize.Model {
    static initiate(sequelize) {
        Comment.init({
            comment: {
                type: Sequelize.STRING,
                allowNull: false,
            }
        }, {
            sequelize,
            timestamps: true,
            modelName: "Comment",
            paranoid: false,
            charset: "utf8mb4",
            collate: "utf8mb4_general_ci"
        })
    }

    static associate(db) {
        // belongsTo ! targetKey : User
        db.Comment.belongsTo(db.User, { foreignKey: 'commenter', targetKey: 'id' });
    }
};

module.exports = Comment;
