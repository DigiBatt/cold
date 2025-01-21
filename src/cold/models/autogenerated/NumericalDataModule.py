
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EncodedDataModule import EncodedData







class NumericalData(EncodedData):
    """
    Class representing the `NumericalData` entity, which inherits from:
    - EncodedData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_888a5dea_3b7d_4dc0_93f2_d4e345a1f903'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumericalData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumericalData(
    
    class_iri='https://w3id.org/emmo#EMMO_888a5dea_3b7d_4dc0_93f2_d4e345a1f903',
    
    class_name='NumericalData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_888a5dea_3b7d_4dc0_93f2_d4e345a1f903',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumericalData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    