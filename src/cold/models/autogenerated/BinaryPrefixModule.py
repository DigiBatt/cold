
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .MetricPrefixModule import MetricPrefix








class BinaryPrefix(MetricPrefix):
    """
    Class representing the `BinaryPrefix` entity, which inherits from:
    - MetricPrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_640ea55c_e9a7_4f23_8aae_5bb4ba867f30'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BinaryPrefix'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BinaryPrefix(
    
    class_iri='https://w3id.org/emmo#EMMO_640ea55c_e9a7_4f23_8aae_5bb4ba867f30',
    
    class_name='BinaryPrefix',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#EMMO_640ea55c_e9a7_4f23_8aae_5bb4ba867f30',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'BinaryPrefix',
        
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    


    
    

    

    