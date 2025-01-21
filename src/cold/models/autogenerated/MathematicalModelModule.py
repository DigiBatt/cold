
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AnalogicalIconModule import AnalogicalIcon



from .MathematicalModule import Mathematical



from .InformationModule import Information







class MathematicalModel(AnalogicalIcon, Mathematical, Information):
    """
    Class representing the `MathematicalModel` entity, which inherits from:
    - AnalogicalIcon, Mathematical, Information

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f7ed665b_c2e1_42bc_889b_6b42ed3a36f0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MathematicalModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MathematicalModel(
    
    class_iri='https://w3id.org/emmo#EMMO_f7ed665b_c2e1_42bc_889b_6b42ed3a36f0',
    
    class_name='MathematicalModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f7ed665b_c2e1_42bc_889b_6b42ed3a36f0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MathematicalModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    