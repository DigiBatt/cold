
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TensileFormingModule import TensileForming



from .ReshapeManufacturingModule import ReshapeManufacturing







class DeepDrawing(TensileForming, ReshapeManufacturing):
    """
    Class representing the `DeepDrawing` entity, which inherits from:
    - TensileForming, ReshapeManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ecf78412_f0ca_4368_9078_559ffe8935d3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DeepDrawing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DeepDrawing(
    
    class_iri='https://w3id.org/emmo#EMMO_ecf78412_f0ca_4368_9078_559ffe8935d3',
    
    class_name='DeepDrawing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ecf78412_f0ca_4368_9078_559ffe8935d3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DeepDrawing',
        alias="class_name"
    )
    

    
    

    

    