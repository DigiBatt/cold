
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialsModelModule import MaterialsModel







class ElectronicModel(MaterialsModel):
    """
    Class representing the `ElectronicModel` entity, which inherits from:
    - MaterialsModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6eca09be_17e9_445e_abc9_000aa61b7a11'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectronicModel'`
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
    obj = ElectronicModel(
    
    class_iri='https://w3id.org/emmo#EMMO_6eca09be_17e9_445e_abc9_000aa61b7a11',
    
    class_name='ElectronicModel',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6eca09be_17e9_445e_abc9_000aa61b7a11',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectronicModel',
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
    

    
    

    

    