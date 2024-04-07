const Sequelize = require("sequelize");

class User extends Sequelize.Model {
    static initiate(sequelize) {
        User.init({
            // ID is made automatically by sequelize
            name: {
                type: Sequelize.STRING(20),
                allowNull: false,
                unique: true
            },
            age: {
                type: Sequelize.INTEGER.UNSIGNED,
                allowNull: false,
            },
            married: {
                type: Sequelize.BOOLEAN,
                allowNull: false,
            },
            comment: {
                type: Sequelize.TEXT,
                allowNull: true,
            },
            created_at: {
                type: Sequelize.DATE,
                allowNull: false,
                defaultValue: Sequelize.NOW
            }
        }, {
           sequelize,
           timestamps: false, // when it is true, createAt, updatedAt are created automatically
           underscored: true, 
           modelName: "User",
           tableName: "users",
           paranoid: false, // deletedAt => It is a soft delete
           charset: 'utf8mb4',
           collate: 'utf8mb4_general_ci',
        })
    }

    static associate(db) {
        // foreignKey : Another, sourceKey : this
        db.User.hasMany(db.Comment, {foreignKey: "commenter", sourceKey: "id"});
    }
}

module.exports = User;
