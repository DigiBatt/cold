
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DoubleLayerModelModule import DoubleLayerModel







class BockrisDevanathanMuellerModel(DoubleLayerModel):
    """
    Class representing the `BockrisDevanathanMuellerModel` entity, which inherits from:
    - DoubleLayerModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4bdd6359_1422_4c50_ac0c_5d8042dd65fc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BockrisDevanathanMuellerModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BockrisDevanathanMuellerModel(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4bdd6359_1422_4c50_ac0c_5d8042dd65fc',
    
    class_name='BockrisDevanathanMuellerModel',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4bdd6359_1422_4c50_ac0c_5d8042dd65fc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BockrisDevanathanMuellerModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    