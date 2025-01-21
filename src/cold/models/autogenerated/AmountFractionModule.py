
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IntensiveModule import Intensive



from .ChemicalCompositionQuantityModule import ChemicalCompositionQuantity



from .RatioQuantityModule import RatioQuantity







class AmountFraction(Intensive, ChemicalCompositionQuantity, RatioQuantity):
    """
    Class representing the `AmountFraction` entity, which inherits from:
    - Intensive, ChemicalCompositionQuantity, RatioQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_04b3300c_98bd_42dc_a3b5_e6c29d69f1ac'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmountFraction'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AmountFraction(
    
    class_iri='https://w3id.org/emmo#EMMO_04b3300c_98bd_42dc_a3b5_e6c29d69f1ac',
    
    class_name='AmountFraction',
    
    iupacReference="example_value",
    
    definition="example_value",
    
    qudtReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_04b3300c_98bd_42dc_a3b5_e6c29d69f1ac',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmountFraction',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    

    
    

    

    