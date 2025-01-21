
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrolyteModule import Electrolyte







class BinaryElectrolyte(Electrolyte):
    """
    Class representing the `BinaryElectrolyte` entity, which inherits from:
    - Electrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4e02d727_07fe_41fd_886c_041317342086'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BinaryElectrolyte'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BinaryElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4e02d727_07fe_41fd_886c_041317342086',
    
    class_name='BinaryElectrolyte',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4e02d727_07fe_41fd_886c_041317342086',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BinaryElectrolyte',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    