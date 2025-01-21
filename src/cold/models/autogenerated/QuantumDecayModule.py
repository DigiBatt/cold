
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalExpansionModule import CausalExpansion







class QuantumDecay(CausalExpansion):
    """
    Class representing the `QuantumDecay` entity, which inherits from:
    - CausalExpansion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6fe3d1d5_4107_4a52_b1d0_3b7c4f871159'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'QuantumDecay'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = QuantumDecay(
    
    class_iri='https://w3id.org/emmo#EMMO_6fe3d1d5_4107_4a52_b1d0_3b7c4f871159',
    
    class_name='QuantumDecay',
    
    conceptualisation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6fe3d1d5_4107_4a52_b1d0_3b7c4f871159',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'QuantumDecay',
        alias="class_name"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    

    
    

    

    