
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NetworkModule import Network







class ProductionSystem(Network):
    """
    Class representing the `ProductionSystem` entity, which inherits from:
    - Network

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_256bb4be_78c6_4f2f_8589_f5e4c8339bbd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ProductionSystem'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ProductionSystem(
    
    class_iri='https://w3id.org/emmo#EMMO_256bb4be_78c6_4f2f_8589_f5e4c8339bbd',
    
    class_name='ProductionSystem',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_256bb4be_78c6_4f2f_8589_f5e4c8339bbd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ProductionSystem',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    