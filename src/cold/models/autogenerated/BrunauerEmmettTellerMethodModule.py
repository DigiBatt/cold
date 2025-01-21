
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GasAdsorptionPorosimetryModule import GasAdsorptionPorosimetry







class BrunauerEmmettTellerMethod(GasAdsorptionPorosimetry):
    """
    Class representing the `BrunauerEmmettTellerMethod` entity, which inherits from:
    - GasAdsorptionPorosimetry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#BrunauerEmmettTellerMethod'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BrunauerEmmettTellerMethod'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BrunauerEmmettTellerMethod(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#BrunauerEmmettTellerMethod',
    
    class_name='BrunauerEmmettTellerMethod',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#BrunauerEmmettTellerMethod',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BrunauerEmmettTellerMethod',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    